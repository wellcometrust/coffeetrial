(function () {
    const onToggleHandler = (e) => {
        e.target.parentNode.classList.toggle('--is-active')
    }

    const initOptions = (container) => {
        container.classList.add('is-hidden')

        const btnToggle = container.querySelector('.js-options-menu-toggle')

        btnToggle.addEventListener('click', onToggleHandler, false)
    }

    const init = () => {
        const options = document.querySelectorAll('.js-options-menu')

        options.forEach(initOptions)
    }

    init()
})()
