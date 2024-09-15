function main() {
    setInterval(() => {
        let date = new Date();
        document.querySelector('.js-output').innerHTML = date.toLocaleTimeString();
    }, 1000);
}

main();
