import React, { useState, useEffect} from "react";
import './Description.css';
function Description (props){
    const [searchTerm, setSearchTerm] = useState('')
    const [data, setData] = useState([{}])
    
    useEffect(() => {
        fetch("/members").then(
        res => res.json()
        ).then(
        data => {
            setData(data)
            console.log(data)
        }
        )
    }, [])

    return (
        <div className="desc-div">
            <input className="search-bar"type="text" 
                placeholder="Enter district (e.g. Texas4)"
                onChange={(event) => {setSearchTerm(event.target.value)
                }}
            />
            {data.filter((val)=> {
                if (searchTerm == "") {
                    return NaN;
                } else if (val.district == searchTerm) {
                    return val
                }
            }).map((val,key) => {
                if (val.party == "democrat")
                {
                    props.handleParty(true)
                }
                else if (val.party == "republican")
                {
                    props.handleParty(false)
                }
                return (
                    <div className="stats"key={key}> 
                        <p className="left">56%</p>
                        <p className="right">42%</p>
                    </div>
                );
            })}
        </div>
    );
}

export default Description;