import { baseActions } from "../utils/base-actions"

export const appStore = {
    constants: {
        CUSTOM_SEPARATOR : 1
    },
    items : {
        form : null
    }
}

export const appActions = {
    store : () => $state.data.app, 
    save  : () => $state.actions.save("app"),
    ...baseActions
}


