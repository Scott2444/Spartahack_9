import React from "react";
import './Description.css';
function Description (props){
    return (
        <div className={props.toggle ? "row-align" : "hide"}>
            <div className="column-align">
                <div className="text-align">
                    <p style={{color:'red'}}>
                        Red: 
                    </p>
                    <p>
                        {props.redAmt}
                    </p>
                    
                </div>
                <div className="text-align">
                    <p style={{color:'blue'}}>
                        Blue: 
                    </p>
                    <p>
                        {props.blueAmt}
                    </p>
                </div>
            </div>
            <div className="column-align">
                <div className="text-align">
                    <p style={{color:'red'}}>
                        Red: 
                    </p>
                    <p>
                        {props.redAmt}
                    </p>
                    
                </div>
                <div className="text-align">
                    <p style={{color:'blue'}}>
                        Blue: 
                    </p>
                    <p>
                        {props.blueAmt}
                    </p>
                </div>
            </div>
        </div>
    )
}

export default Description;