import m from "mithril"
import "./FormScreen.scss"
import { createForm, Field } from "../../utils/forms"
import z from "zod"
import { appStore } from "../../stores/app"

export default {
  oninit() {
    this.form = createForm(z.object({
      username: z.string().min(8), 
      password: z.string().min(8), 
      confirmPassword: z.string(),
      firstName: z.string().min(1),
      lastName: z.string().min(1), 
      email: z.email(), 
      gender: z.enum(["MALE", "FEMALE"]),
      birthdate: z.date(), 
      bio: z.string().min(10) 
    })
    .refine((data) => data.password == data.confirmPassword, {
      message: "Passwords don't match",
      path: ["confirmPassword"]
    })
    )

    this.form.linkSource("registration", () => appStore, {
      username: null, 
      password: null, 
      confirmPassword: null, 
      firstName: null, 
      lastName: null, 
      email: null, 
      gender: null, 
      birthdate: null, 
      birthdate: null, 
      bio: null
    })

    window.$form = this.form
  },
  
  view() {
    return m("div.FormScreen",  [
      m("div.header", m("b","Registration Form")), 
      m("div.form", [
        m(Field, {
          form: this.form, 
          field: ["username"], 
          render (binder, errors, value) {
            return m("div.field-item", [
              m("div.label", m("b", "Username")), 
              m("div.value", m("input.value-input", { ...binder, value })), 
              m("div.errors", JSON.stringify(errors))
            ])
          }
        }),

        m(Field, {
          form: this.form, 
          field: ["password"], 
          render (binder, errors, value) {
            return m("div.field-item", [
              m("div.label", m("b", "Password")), 
              m("div.value", m("input.value-input", { ...binder, type: "password", value })), 
              m("div.errors", JSON.stringify(errors))
            ])
          }
        })
      ])
    ])
  }
}
