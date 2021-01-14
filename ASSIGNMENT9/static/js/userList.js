
fetch('https://reqres.in/api/users?page=2').then(response => response.json()).then(responseJSON => createUsersList(responseJSON.data)).catch(err => console.log(err));

function createUsersList(users){
console.log(users);
}

//todo bladef



fetch('https://reqres.in/api/users?page=2').then(response => response.json()).then(responseJSON => createUsersList(responseJSON.data)).catch(err => console.log(err));

function createUsersList(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for (let user of users){
        const section = document.createElement('section');
        section.innerHTML = `
        <div class="user_">
            <img class="img" src="${user.avatar}" alt="picture"/>
            <br>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
            <br><br>
                
        </div> 
        `
        curr_main.appendChild(section);


    }
}