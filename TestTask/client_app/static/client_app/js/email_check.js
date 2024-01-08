const HOST = new URL(current_url).origin
const API_EMAIL_CHECK_API = api_check_email
const API_EMAIL_SAVE = api_save_email

const form = document.forms['email_check']
const check_email_result = document.querySelector('.check-email__content')
const btn_save = document.querySelector('.btn__save')
const btn_change = document.querySelector('.btn__change')
const btn_del = document.querySelector('.btn__del')
const p = document.createElement('p')
const textarea = document.createElement('textarea')
let json_to_send = ''
const error = document.querySelector('.error')

form.addEventListener('submit', async event => {
    event.preventDefault()
    const email = form.email.value


    const response = await fetch(HOST + API_EMAIL_CHECK_API + `?email=${email}`)
    const response_json = await response.json()

    if (response_json.api) {
        showError('Api is inccorect')
    } else {
        json_to_send = response_json

        p.innerText = JSON.stringify(response_json, null, 2)

        check_email_result.append(p)
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

btn_del.addEventListener('click', event => {
    delResult()
})

btn_save.addEventListener('click', async event => {
    if (!json_to_send) {
        showError('Upps... nothing to send')
        return
    }

    const body = {
        json_response: json_to_send
    }

    const response = await fetch(HOST + API_EMAIL_SAVE, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify(body)
    })


    if (response.ok) {
        showAccept('Email has been saved')
        delResult()

    }
})


function showError(text) {
    error.classList.add('show')
    error.innerText = text
    setTimeout(() => {
        error.classList.remove('show')
    }, 5000)
}

function showAccept(text) {
    error.classList.add('accept')
    error.classList.add('show')
    error.innerText = text
    setTimeout(() => {
        error.classList.remove('accept')
        error.classList.remove('show')

    }, 5000)
}

function delResult() {
    check_email_result.innerHTML = ''
    p.innerText = ''
    json_to_send = ''
    if (btn_change.classList.contains('change')) {
        btn_change.classList.remove('change')
    }
}