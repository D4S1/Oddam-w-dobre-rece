const form = document.querySelector("form#donation-form")

form.addEventListener('change', function (e){
    const target = e.target
    console.log(target)
    console.log(target.name)
})
