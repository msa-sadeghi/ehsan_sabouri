import { useState } from "react"
function ProductCard(){
    const [user, setUser] = useState(
        {
            name:'ali',
            age:37,
            email:'ali@gmail.com'
        }
    )
    const changeName =  (newName)=>{
        setUser({
            ...user,
            name:newName
        })
    }
    const changeAge =  (newAge)=>{
        setUser({
            ...user,
            age:newAge
        })
    }
    return (
        <>
            <input type="text" value={user.name}
            onChange={(e)=>changeName(e.target.value)}
            />
            <p>name : {user.name} </p>
            <input type="text" value={user.age}
            onChange={(e)=>changeAge(e.target.value)}
            />
            <p>age : {user.age} </p>
            <p>email : {user.email} </p>
        </>
    )
}

export default ProductCard