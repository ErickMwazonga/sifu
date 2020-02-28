const get_repeat_count = lst => {
    const lst_frequency = {};
    let count = 0;

    lst.forEach((value, idx) => {
        lst_frequency[value] = lst_frequency[value] ? lst_frequency[value] + 1 : 1;

        const c = lst_frequency[value];

        if
    })

    console.log(lst_frequency)
}

get_repeat_count([3, 5, 6, 3, 3, 5])