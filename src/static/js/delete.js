

window.onload = ()=>{
    const main = document.querySelector("main");

    const submit = document.getElementById("delete_button");
    submit.addEventListener("click", async (e) => {
        e.preventDefault();

        const section = document.querySelector("section");   
        const id = document.querySelector("input[type='hidden']").value;
        const body = {id};

        const response = await fetch(
            "/cars/delete",
            {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(body)
            }
        )

        const data = await response.json();

        if(data.success){
            const successContainer = document.createElement("div")
            successContainer.textContent = "voiture supprimée avec succés.";
            successContainer.classList.add("success_container");
            main.removeChild(section);
            main.appendChild(successContainer);
        }else{
            const errorContainer = document.createElement("div")
            errorContainer.textContent = data.message;
            errorContainer.classList.add("error_container");
            main.removeChild(section);
            main.appendChild(errorContainer);
        }

    })
}