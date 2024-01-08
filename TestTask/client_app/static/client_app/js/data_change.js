const HOST = new URL(current_url).origin
const API_USER_API = api_change_api_user
const API_CHANGE_EMAIL = api_change_email
const API_CHANGE_DOMAIN = api_change_domain

const api_list = document.querySelector('.api-list')
const api_list_li = api_list.querySelectorAll('li')
const email_list = document.querySelector('.email__list')
const email_list_li = email_list.querySelectorAll('li')
const domain_list = document.querySelector('.domain__list')
const domain_list_li = domain_list.querySelectorAll('li')
const popup_message = document.querySelector('.popup_message')

for (let li of api_list_li) {

    const btn_active = li.querySelector('.btn__active')
    const btn_change = li.querySelector('.btn__change')
    const btn_del = li.querySelector('.btn__del')
    const api_key = li.querySelector('.api-list__api-key')
    const pk_api = li.dataset.pk

    btn_active.addEventListener('click', async event => {
        const response = await fetch(HOST + API_USER_API + '/' + pk_api + '/' + 'active', {
            method: 'PUT'
        })

        const response_json = await response.json()

        if (response_json.success) {
            for (let li of api_list_li) {
                li.classList.remove('active')
            }

            li.classList.add('active')
        }
    })

    btn_change.addEventListener('click', async event => {
        const value_api = api_key.innerText
        const div = document.createElement('div')
        const input = document.createElement('input')
        const button_done = document.createElement('button')

        input.value = value_api
        button_done.innerText = '✔'
        div.classList.add('change-block')

        div.append(input)
        div.append(button_done)

        api_key.replaceWith(div)

        button_done.onclick = async event => {
            api_key.innerHTML = `<span>${input.value}</span>`
            div.replaceWith(api_key)



            fetch(HOST + API_USER_API + '/' + pk_api, {
                method: 'PUT',
                headers: {
                    'content-type': 'application/json',
                },
                body: JSON.stringify({
                    'api_key': input.value
                })
            })
        }

    })

    btn_del.addEventListener('click', async event => {
        const response = await fetch(HOST + API_USER_API + '/' + pk_api, {
            method: 'DELETE'
        })

        if (response.ok) {
            li.remove()
        }
    })

}

for (let li of email_list_li) {
    const btn_del = li.querySelector('.btn__del')
    const pk = li.dataset.pk

    btn_del.addEventListener('click', async event => {

        const response = await fetch(HOST + API_CHANGE_EMAIL + pk,
            {
                method: 'DELETE'
            })

        if (response.ok) {
            showAccept('Email has been deleted')
            li.remove()
        }

    })

}

for (let li of domain_list_li) {
    const btn_del = li.querySelector('.btn__del')
    const pk = li.dataset.pk



    btn_del.addEventListener('click', async event => {
        const response = await fetch(HOST + API_CHANGE_DOMAIN + pk,
            {
                method: 'DELETE'
            })

        if (response.ok) {
            showAccept('Domain has been deleted')
            li.remove()
        }

    })
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

