import React from "react";
import './Box.css'
import Description from "./Description.js";
import {useState} from 'react';

function Box (props) {
    
    const [toggle, setToggle] = useState(false)

    const handleClick = () => {
        setToggle(prevToggle => !prevToggle)
    }

    return (
        <div className="box-div">
            <p className={toggle ? "": "hide"}>Image</p>
            <button onClick={handleClick}className="button">Reveal</button>
            <Description toggle={toggle}redAmt={10}blueAmt={15}/>
        </div>
    )
}

export default Box;