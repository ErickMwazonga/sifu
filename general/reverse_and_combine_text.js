const reverse_and_combine_text = text => {
    let result = '';
    const input = text.split(' ');

    for(let i = 0; i < input.length; i++){
        const a = input[i]
        const b = input[i+1] || ''

        result = `${result}${b}${a}`;
        i += 1;
    }

    console.log(result);
    return result;
}


reverse_and_combine_text("abc def") //  "cbafed"
reverse_and_combine_text("abc def ghi jkl") // defabcjklghi
reverse_and_combine_text("dfghrtcbafed") // "dfghrtcbafed")
reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12  44") // "trzwqfdstrteettr45hh4325543544hjhjh21lllll")