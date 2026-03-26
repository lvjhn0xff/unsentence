
export function group(items, groupKey, key) {
    let indexed = {} 
    for(let item of Object.values(items)) {
        if(!(item[groupKey] in indexed)) {
            indexed[item[groupKey]] = {}
        }
        indexed[item[groupKey]][item[key]] = null

    }
    return indexed
}