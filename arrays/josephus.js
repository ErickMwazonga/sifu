const a = (n, k) => {
    let people = [];
    let victims = [];

    for(let i=1; i<=n; i++) {
        people.push(i)
    }

    let pplTemp = [...people];
    let nextKill = 0;

    people.forEach((item, idx) => {
        len = pplTemp.length;
        nextKill = k - 1;

        if(nextKill < len) {
            victims.push(pplTemp[nextKill]);
            pplTemp.splice(nextKill, 1)
            
            rest = pplTemp.splice(nextKill)
            pplTemp.unshift(...rest)
        } else {
            nextKill = 0;
            victims.push(pplTemp[nextKill]);
            pplTemp.splice(nextKill, 1)
        }
    })

    return victims.pop();
}

console.log(a(100, 1))