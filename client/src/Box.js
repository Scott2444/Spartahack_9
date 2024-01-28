import React from "react";
import './Box.css'
import Description from "./Description.js";
import {useState} from 'react';
import photoholder from './imgs/original.png';
import democrat from './imgs/democrat.png';
import republican from './imgs/republican.png';

function Box (props) {
    const [party, setParty] = useState(true)
    const [toggle, setToggle] = useState(false)

    const handleParty = (p) => {
        setParty(p)
    }

    const handleClick = () => {
        setToggle(prevToggle => !prevToggle)
    }

    return (
        <div className="box-div">
            <div className="image-div">
                <img className={toggle ? "hide": "appear"}src={photoholder}width="250"height="250"></img>
                <img className={toggle ? "appear-image": "hide"}src={party ? democrat : republican}width="250"height="250"></img>
            </div>
            <button onClick={handleClick}className="button">Reveal</button>
            <div className={toggle ? "appear" :"hide-desc"}>
                {/* <div className="desc-div"> */}
                    <Description handleParty={handleParty}redAmt={10}blueAmt={15}/>
                {/* </div> */}
            </div>
        </div>
    )
}

export default Box;