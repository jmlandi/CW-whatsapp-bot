const getName = (name) => {

    // preparing variables
    name = name.trim().split(' ');
    let toBeRemoved = []
    let contCharRemoved = 0
    
    // Fixing name and removing not AlphaNumeric chars
    for (let i in name) {
        let newName = ""
        for (let j in name[i]) {
            if (name[i][j].search(/^[a-zA-z0-9]+$/) != -1) {
                if (j == 0) {
                    newName += name[i][j].toUpperCase()
                } else {
                    newName += name[i][j].toLowerCase()
                }
            }
        }
        name[i] = newName

        // check if it's a valid name
        if (name[i].search(/^[a-zA-Z0-9]+$/) == -1) {
            toBeRemoved += i
        }


    }

    // fetching index to remove empty strings
    for (let k in toBeRemoved) {
        name.splice((toBeRemoved[k] - contCharRemoved),1)
        contCharRemoved += 1
    }

    let response = {"name": name};

    return JSON.stringify(response);
}

console.log(getName("jHon     doE😉  "));