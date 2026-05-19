

window.onload = ()=>{
    console.log("JAVASCRIPT")
    const main = document.querySelector("main");

    const submit = document.getElementById("submit_button");
    submit.addEventListener("click", async (e) => {        
        e.preventDefault();
        
        const form = document.querySelector("form");       
        const id = document.querySelector("input[type='hidden']").value;
        const brand = document.querySelector("input[name='brand']").value;
        const model = document.querySelector("input[name='model']").value;
        const body = {id, brand, model};

        const response = await fetch(
            "/cars/update",
            {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(body)
            }
        )

        const data = await response.json();

        if(data.success){
            const successContainer = document.createElement("div")
            successContainer.textContent = "voiture modifiée avec succés.";
            successContainer.classList.add("success_container");
            main.removeChild(form);
            main.appendChild(successContainer);
        }else{
            const errorContainer = document.createElement("div")
            errorContainer.textContent = data.message;
            errorContainer.classList.add("error_container");
            main.removeChild(form);
            main.appendChild(errorContainer);
        }

    })
}