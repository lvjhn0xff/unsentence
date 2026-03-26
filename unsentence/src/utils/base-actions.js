export const baseActions = {
    create(item) {
        let store = this.store()
        store._id += 1 
        item.id = store._id 
        store.items[store._id] = item
        
        for(let group of store.groups) {
            let groupName = group[0]
            let grouper = group[1]
            store[groupName][item[grouper]][store._id] = null 
        }

        this.save()
    },

    delete(id) {
        console.log("Deleting", id)
        let store = this.store()

        let item = store.items[id]

        for(let group of store.groups) {
            let groupName = group[0]
            let grouper = group[1]
            delete store[groupName][item[grouper]][item.id]
        }

        delete store.items[id]

        this.save()
    },

    read(id) {
        let store = this.store()
        return store.items[id]
    },

    updateItem(id, callback) {
        let store = this.store()
        callback(store.items[id])
        this.save()
    },

    update(callback) {
        let store = this.store()
        callback(store.items)
        this.save()    
    },
    

    of(group, id) {
        let store = this.store()
        let self = this
        return Object.keys(store[group][id]).map(x => self.read(x))
    }
}

export function setFields(object, data) {
    for(let key in data) {
        object[key] = data[key]
    }
}