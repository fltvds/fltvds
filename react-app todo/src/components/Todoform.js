import React, { useState, useEffect, useRef } from 'react';

function Todoform(props) {
    const [input, setInput] = useState(props.edit ? props.edit.value : '');

    const inputRef = useRef(null)

    useEffect(() => {
        inputRef.current.focus()
    })

    const handleChange = e =>{
        setInput(e.target.value);
    }

    const handleSubmit = e =>{
        e.preventDefault();

        props.onSubmit({
            id: Math.floor(Math.random()*10000),
            text: input
        });

        setInput('');
    }

    return (
        <form className="todo-form" onSubmit={handleSubmit}>
            {props.edit ? (
            <>
            <input type="text" placeholder="Kirjuta siin" 
            value={input} name="text" className="todo-input edit" 
            onChange={handleChange} ref={inputRef}/>
            <button className="todo-button edit">Salvesta</button> 
            </>) : 
            (
                <>
                <input type="text" placeholder="Kirjuta siin" 
            value={input} name="text" className="todo-input" 
            onChange={handleChange} ref={inputRef}/>
            <button className="todo-button">Lisa</button> 
            </>
            )}
            
            
        </form>
        
    );
}

export default Todoform;
