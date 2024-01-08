const API_DOMAIN_CHECK = api_check_domain
const API_DOMAIN_SAVE = api_save_domain
const HOST = new URL(current_url).origin

const form = document.forms['domain_check']
const check_domain_result = document.querySelector('.domain-check__content')
const btn_save = document.querySelector('.btn__save')
const btn_change = document.querySelector('.btn__change')
const btn_del = document.querySelector('.btn__del')
const p = document.createElement('p')
const textarea = document.createElement('textarea')
let json_to_send = ''
const popup_message = document.querySelector('.popup_message')

console.log(form)
console.log('asldf')

form.addEventListener('submit', async event => {
    event.preventDefault()
    const domain = form.domain.value


    const response = await fetch(HOST + API_DOMAIN_CHECK + `?domain=${domain}`)
    const response_json = await response.json()
    if (response_json.api) {
        showError('Api is inccorect')
    } else {

        json_to_send = response_json

        p.innerText = JSON.stringify(response_json, null, 2)

        check_domain_result.append(p)
    }
})

btn_change.addEventListener('click', event => {

    if (!p.innerText) return;

    btn_change.classList.toggle('change')


    if (btn_change.classList.contains('change')) {
        const value = p.innerText
        textarea.innerText = value

        p.replaceWith(textarea)
    } else {
        const value = textarea.value

        try {
            json_to_send = JSON.parse(value)
            p.innerText = JSON.stringify(json_to_send, null, 2)
        } catch {
            json_to_send = ''
            showError('Something went wrong with changing json')
            return
        }

        textarea.replaceWith(p)
    }
})


btn_save.addEventListener('click', async event => {
    if (!json_to_send) {
        showError('Upps... nothing to send')
        return
    }

    const body = {
        domain_json: json_to_send
    }

    const response = await fetch(HOST + API_DOMAIN_SAVE, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify(body)
    })


    if (response.ok) {
        showAccept('Domain has been saved')
        delResult()

    }
})


btn_del.addEventListener('click', event => {
    delResult()
})


function showError(text) {
    popup_message.classList.add('show')
    popup_message.classList.add('error')
    popup_message.innerText = text
    setTimeout(() => {
        popup_message.classList.remove('show')
        popup_message.classList.remove('error')

    }, 5000)
}

function showAccept(text) {
    popup_message.classList.add('accept')
    popup_message.classList.add('show')
    popup_message.innerText = text
    setTimeout(() => {
        popup_message.classList.remove('accept')
        popup_message.classList.remove('show')
    }, 5000)
}

function delResult() {
    check_domain_result.innerHTML = ''
    p.innerText = ''
    json_to_send = ''
    if (btn_change.classList.contains('change')) {
        btn_change.classList.remove('change')
    }
}