const form = document.querySelector("form#donation-form")
const organisations = Array.from(document.querySelectorAll("div#organisation"))
const summary = document.querySelector("#step-4-btn")
const end_btn = document.querySelector("#end-btn")

let bags = document.querySelector("#s-bag")
let organisation = document.querySelector("#s-organisation")
let address = document.querySelector("#s-address")
let city = document.querySelector("#s-city")
let zip_code = document.querySelector("#s-zip-code")
let phone = document.querySelector("#s-phone")
let pick_up_date = document.querySelector("#s-date")
let pick_up_time = document.querySelector("#s-time")
let notice = document.querySelector("#s-notice")

function remove(arr, element){
    if (arr.includes(element)){
        let index = arr.indexOf(element)
        return arr.splice(index, 1)
    }
}

function categories_to_pk(arr){
    // convert list of inputs to list of input's values
    const new_arr = []
    arr.forEach(ele => {
        new_arr.push(ele.value)
    })
    return new_arr
}

function categories_to_name(arr){
    // convert list of inputs to str of input's category name
    let new_str = ""
    arr.forEach(ele => {
        new_str += ele.dataset.category + ", "
    })
    return new_str
}


function change_display(arr){
    arr.forEach(ele => {
     let o_cat = ele.dataset.categories.split(',')
     let inc = false
     if(categories.length !== 0){
        inc = categories_to_pk(categories).every(val => o_cat.includes(val));
     }
     if(inc){
         ele.style.display = null
     }
     else{
         ele.style.display = 'none'
     }
})
}

// list of category inputs
let categories = Array.from(document.querySelectorAll('input[name=category]')).filter(ele => ele.checked===true)
change_display(organisations)

let chosen_organisation = document.querySelector('input[name=organisation]:checked')

form.addEventListener('change', function (e){
    const target = e.target

    // STEP 3 ORGANISATIONS
    if(target.name === "category"){
        //if category is checked or not
        if (target.checked){
            categories.push(target)
        }
        else{
            remove(categories, target)
        }

        // loop which check if organisation has checked categories
        change_display(organisations)
    }

    else if (target.name === 'organisation'){
        chosen_organisation = document.querySelector('input[name=organisation]:checked')
    }
})

summary.addEventListener('click', function (e){
    const target = e.target
    // dopisać dataset do kategorii i organizacji z nazwami, żeby się ładnie wyświetlało
    // wgl najlepiej napisać funkcję, która w zależnie od trybu zwraca listę zaznaczonych kategorii, jako pk albo nazwa
    bags.innerText = document.querySelector("#v-bags").value + " worków " + categories_to_name(categories)

    // hint dotyczący brania checked z radio input
    // https://developer.mozilla.org/en-US/docs/Web/CSS/:checked
    // Dla fundacji "Mam marzenie" w Warszawie
    organisation.innerText = "Dla " + chosen_organisation.dataset.type + ' "' + chosen_organisation.dataset.organisation + '"'

    address.innerText = document.querySelector("#v-address").value
    city.innerText = document.querySelector("#v-city").value
    zip_code.innerText = document.querySelector("#v-zip-code").value
    phone.innerText = document.querySelector("#v-phone").value
    pick_up_date.innerText = document.querySelector("#v-date").value
    pick_up_time.innerText = document.querySelector("#v-time").value
    let v_notice = document.querySelector("#v-notice").value
    if(v_notice){
        notice.innerText = v_notice
    }

})

end_btn.addEventListener("click", function (e){
    form.submit()
})

// jak się przeładowuje stronę, to nie zapamiętuje kategorii
// poprawić, żeby wyświetlały się nazwy organizacji i kategorii
// jak wziąć zaznaczony radio input
