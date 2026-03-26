/** Import Stylesheet */ 
import "./main.scss"

/** Load State */
import { state } from "./state"
state.actions.loadAll()

/** Aside Script */
import "./utils/aside.js"

import _ from "lodash"
window._ = _

/** Create and Mount Application */
import m from "mithril"
import { routes } from "./routes"
const $app = document.getElementById("app") 
m.route($app, "/home", routes)

