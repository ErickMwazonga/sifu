const VOWELS = ['a', 'e', 'i', 'o', 'u'];

const distanceToVowel = _str => {
    const split = _str.toLowerCase().split('');

    return split.map((letter, i) => {
        if (VOWELS.includes(letter)) return 0;

        let distance = 1;

        while (true) {
            if (VOWELS.includes(split[i - distance]) || VOWELS.includes(split[i + distance])) {
                break;
            }
            distance++;
        }
        return distance;
    })
}

console.log(distanceToVowel('abdsesduasa'))