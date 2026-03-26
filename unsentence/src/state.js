import { stores } from "./stores"

export const state = {
    data : stores,
    actions : {
        update(context, action) {
            stateActions.update(state, context, action)
        },
        save(context) {
            let contextStr = JSON.stringify(state.data[context])
            return localStorage.setItem(context, contextStr)
        }, 
        load(context) {
            if(context in localStorage) {
                console.log("--- Loading", context)
                
                let data = JSON.parse(localStorage.getItem(context))

                // Load data.
                for(let contextItem in data) {
                    state.data[context][contextItem] = data[contextItem]
                }

            }
        },
        loadAll() {
            for(let context in state.data) {
                state.actions.load(context)
            }
        }
    }
}


window.$state = state