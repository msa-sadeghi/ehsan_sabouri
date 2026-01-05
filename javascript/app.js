// fetch('https://jsonplaceholder.typicode.com/users')
// .then(
//     response => response.json()
// )
// .then(data => console.log(data))
// .catch(error => console.log("error"))



async function  getUsers(url) {
    try{
        const response = await fetch(url)
    if(!response.ok){
        throw new Error("er")
    }
    const users =  await response.json()

    console.log(users)
    }
    catch(error){
        console.log(error.message)
    }
}

getUsers('https://jsonplaceholder.typicode.com/users')

async function createPost() {
    
    const newPost = {
        title:'test post',
        body:'this is a test post',
        userId:1
    }

    const response = await fetch('https://jsonplaceholder.typicode.com/posts'
        ,{
            method:'POST',
            headers :{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(newPost)
        }
    )
    const data = await response.json()
    console.log(data)
}

createPost()

// تمرین ۱

// یک تابع بنویس:

// لیست پست‌ها را بگیرد

// فقط عنوان‌ها را چاپ کند

// تمرین ۲

// یک پست با عنوان دلخواه خودت ارسال کن