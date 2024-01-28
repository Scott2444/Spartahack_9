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
                placeholder="Enter a district number..."
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
                    <div key={key}> 
                        <p>{val.party}</p>
                    </div>
                );
            })}
        </div>
    );
}

export default Description;