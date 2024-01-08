const API_CHANGE_DOMAIN = api_change_domain
const HOST = new URL(current_url).origin
const PK = current_domain_pk

let domainDataElement = document.getElementById('domain-data');
let domainData = JSON.parse(domainDataElement.textContent || domainDataElement.innerText);
const button_save = document.querySelector('.btn__save')
const textarea = document.querySelector('textarea')
const popoup_message = document.querySelector('.popoup_message')
textarea.innerText = JSON.stringify(domainData)



button_save.addEventListener('click', async event => {
    let is_valid = false
    const json_textarea = textarea.value.trim()
    let json_to_send = ''


    try {
        json_to_send = JSON.parse(json_textarea)
        is_valid = true

    } catch (error) {
        is_valid = false
    }

    if (is_valid) {
        const response = await fetch(HOST + API_CHANGE_DOMAIN + PK, {
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(
                {
                    'domain_json': json_to_send
                }
            ),
            method: 'PUT'
        })

        const response_json = await response.json()


        if (response.ok) {
            showAccept('domain has been changed')
        } else {
            showError('Something went wrong')
        }

    } else {
        showError('Your json inncorrect')
    }


})

btn_del.addEventListener('click', async event => {

})

function showError(text) {
    popoup_message.classList.add('show')
    popoup_message.classList.add('error')

    popoup_message.innerText = text
    setTimeout(() => {
        popoup_message.classList.remove('error')
        popoup_message.classList.remove('show')
    }, 5000)
}

function showAccept(text) {
    popoup_message.classList.add('accept')
    popoup_message.classList.add('show')
    popoup_message.innerText = text
    setTimeout(() => {
        popoup_message.classList.remove('accept')
        popoup_message.classList.remove('show')

    }, 5000)
}
