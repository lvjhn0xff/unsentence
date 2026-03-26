
export function classBinder(classes) {
    let classList = []
    for(let class_ in classes) {
        if(classes[class_]) {
            classList.push(class_)
        }
    }
    return classList.join(" ")
}