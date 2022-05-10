const form = document.querySelector("form#donation-form")
const organisations = Array.from(document.querySelectorAll("div#organisation"))
const summary = document.querySelector("#step-4-btn")

// poprawić zmienną categories, żeby nie była pusta tylko querySelectorAll i dodawać tylko checked
const categories = []

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

form.addEventListener('change', function (e){
    const target = e.target
    console.log(target.name)

    // STEP 3 ORGANISATIONS
    if(target.name === "category"){
        //if category is checked or not
        if (target.checked){
            categories.push(target.value)
        }
        else{
            remove(categories, target.value)
        }

        // loop which check if organisation has checked categories
        organisations.forEach(organisation =>{
            let o_cat = organisation.dataset.categories.split(',')

            let inc = false
            if(categories.length !== 0){
                inc = categories.every(val => o_cat.includes(val));
            }
            // changes visibility of organisation
            if(inc){
              organisation.style.display = null
            }
            else{
                organisation.style.display = 'none'
                }
        })
    }
})

summary.addEventListener('click', function (e){
    const target = e.target
    // dopisać dataset do kategorii i organizacji z nazwami, żeby się ładnie wyświetlało
    // wgl najlepiej napisać funkcję, która w zależnie od trybu zwraca listę zaznaczonych kategorii, jako pk albo nazwa
    bags.innerText = document.querySelector("#v-bags").value + " worków " + categories

    // hint dotyczący brania checked z radio input
    // https://developer.mozilla.org/en-US/docs/Web/CSS/:checked
    // organisation.innerText = document.querySelector("#v-organisation").value

    address.innerText = document.querySelector("#v-address").value
    city.innerText = document.querySelector("#v-city").value
    zip_code.innerText = document.querySelector("#v-zip-code").value
    pick_up_date.innerText = document.querySelector("#v-date").value
    pick_up_time.innerText = document.querySelector("#v-time").value
    let v_notice = document.querySelector("#v-notice").value
    if(v_notice){
        notice.innerText = v_notice
    }

})

// jak się przeładowuje stronę, to nie zapamiętuje kategorii
// poprawić, żeby wyświetlały się nazwy organizacji i kategorii
// jak wziąć zaznaczony radio input
