import React from 'react'
import Image from 'next/image'
import Link from 'next/link'

const Hero = () => (
    <>
    <div className=' flex flex-row'>
        <div id='first-header' className=' flex flex-col ml-80 mt-44 relative'>
            <div className='circle-1 absolute w-32 rounded-full aspect-square -ml-14 -mt-[40px]' />
            <div className=' text-6xl font-bold'>
                <div className=' flex flex-row'>
                    <h1>Explore the</h1>   
                    <h1 className=' ml-4 text-transparent bg-clip-text bg-gradient-to-br from-blue-600 to-purple-800' >cosmos</h1>                     
                </div>

                <h1>create connections.</h1>          
            </div>
            <p className=' w-[430px] mt-4 font-light text-xl bg-clip-text'>
                Effortlessly gather email addresses
                from the galaxy with our cutting-edge 
                web scraping tools.
            </p>
            <div className=' flex flex-row mt-6 space-x-8 text-md '> 
                <Link className=' w-32 h-10 bg-purple-700 rounded-md text-center justify-center' href='/signup'>
                    <p className=' mt-2'>Get Started</p>
                </Link>
                <div>
                    <button className=' w-32 h-10 bg-transparent border-2 border-purple-600 rounded-md'>
                        <p className=' text-purple-500'>Try Now</p>
                    </button>                    
                </div>

            </div>
            <div className=' bg-gradient-to-b from-[#B5B5B5] to-[#0090AF] w-32 h-32 rounded-full mt-60 ml-12'>
                <div className=' w-32 h-32 absolute bg-gradient-to-bl from-purple-800 opacity-60 rounded-full'>
                    
                </div>
            </div>
        </div>
        <div className=' ml-44 mt-20 bg-gradient-to-b from-black w-[550px] h-[600px] rounded-3xl border-purple-950 border-opacity-20 border-2'>

        </div>
    </div>
    </>
    
)

export default Hero