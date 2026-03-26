import _ from "lodash";
import { fromPath } from "./helpers";


export function createForm(zodSchema) {
    return {
        schema: zodSchema,
        data: {},
        validData: null,
        errors: null,
        validateHooks : {},
        updateHooks: {},
        touched: new Set(),
        
        handleResults(validationResult) {
            // Handle results
            if(validationResult.success) {
                this.validData = validationResult.data
                this.errors = []
            } else {
                this.errors = JSON.parse(validationResult.error.message)
            }

            this.runHooks(this.validateHooks)
        },

        validateAll() {
            // Validate
            const validationResult = zodSchema.safeParse(this.data);    

            // Handle Results
            this.handleResults(validationResult)
        },

        canSubmit() {
            return this.errors == null || this.errors?.length == 0
        },
        addHook(context, name, callback) {
            context[name] = callback
        },
        removeHook(context, name) {
            delete context[name]
        },
        runHooks(context) {
            for(let item in context) {
                context[item]()
            }
        },
        linkSource(name, source, data) {
            let source_ = source()
            source_[name] = data 
            let self = this

            this.addHook(this.updateHooks, "sync-data", () => {
                for(let key in self.data) {
                    source_[name][key] = self.data[key]
                }
            })
        }
    }
}

export function setFormField(form, field, value) {
    if(field.length == 1) {
        form.data[field] = value
    } else {
        let base = form.data 
        let index = 0
        while (index < field.length - 1) {
            base = base[field[index]]
            index += 1
        }
        base[field.at(-1)] = value
    } 
}

export function getFormField(form, field) {
    if(field.length == 1) {
        return form.data[field] 
    } else {
        let base = form.data 
        let index = 0
        while (index < field.length) {
            base = base[field[index]]
            index += 1
        }
        return base
    } 
}

export const Field = {    
    view(vnode) {
        let form = vnode.attrs.form 
        let field = vnode.attrs.field
        let validateWith = vnode.attrs.validateWith
        let render = vnode.attrs.render 

        form.validateWith = validateWith
        
        let debounceValidate = _.debounce(() => {
            form.validateAll()
        }, 300)
        
        let normalize = (x) => x

        let binder = { 
            oninput (e) {
                form.touched.add(fromPath(field))
                form.runHooks(form.addHooks)
                setFormField(form, field, normalize(e.target.value))
                debounceValidate()
            },
            onchange (e) {
                form.touched.add(fromPath(field))
                form.runHooks(form.updateHooks)  
                setFormField(form, field, normalize(e.target.value))
                debounceValidate()
            },
            value: getFormField(form, normalize(field))
        } 
        
        let errors = form.errors?.filter(error => _.isEqual(field, error.path)) || []
        let value  = _.get(form.validData, field)
        let fieldName = fromPath(field)

        if(!form.touched.has(fieldName)) {
            errors = null
        }

        return render(binder, errors, value)
    }
} 