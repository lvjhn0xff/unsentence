
export function index(items, key) {
    let indexed = {} 
    for(let item of Object.values(items)) {
        indexed[item[key]] = item 
    }
    return indexed
}