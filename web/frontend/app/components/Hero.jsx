import React from 'react'
import Image from 'next/image'
import styles from './comps.css'
import Link from 'next/link'

const Hero = () => (
    <>
    <div className=' absolute'>
            <div id='purp-blur' className='absolute  bg-[#BA21AB] blur-[250px] opacity-25 w-[906px] h-[750px] ml-[1150px] -mt-[437px]' />
            <div id='blue-blur' className='absolute bg-[#6473FF] blur-[500px] w-[633px] h-[659px] rounded-full -ml-[400px] mt-[500px]' />
        </div>
        <div className=' flex flex-row'>
            <div id='first-header' className=' flex flex-col ml-80 mt-44 relative'>
            <div className='circle-1 absolute w-32 rounded-full aspect-square -ml-14 -mt-[60px]' />
            <button className=' ml-[340px] w-24 h-6 bg-[#C8B65B] text-black font-semibold'> Login </button>
            <div className=' text-5xl font-bold'>
                <h1>Explore the cosmos</h1>
                <h1>create connections.</h1>          
            </div>
            <p className=' w-[290px] mt-4 font-light text-lg'>
                Effortlessly gather email addresses
                from the galaxy with our cutting-edge 
                web scraping tools.
            </p>
            <div className=' flex flex-row mt-6 ml-16 space-x-8 text-lg'> 
                <button className=' w-32 h-12 bg-[#5A42D5] rounded-md'>Get Started</button>
                <button className=' w-32 h-12 border-[#5A42D5] border-[3px] rounded-md text-[#5A42D5]'>Buy Now</button>
            </div>
            </div>
            <div className=' relative ml-96  w-96 h-[370px] mt-60 '>
            <Image className=' ' src='/blue-planet.png' fill />
            </div>
        </div>
        <div id='section-2' className=' flex flex-row relative '>
            <div className=' bg-[#353E8E] rounded-full w-[523px] aspect-square -ml-64 -mt-24 absolute blur-[2px]' />
            <div className=' flex flex-col items-center w-screen'>
            <div className=' mt-24 flex flex-row'>
                <Link href='/' className=' text-[#5A42D4] hover:underline font-semilight' >View our quick start guide </Link>
                <div className=' ml-2 w-5 h-4 relative mt-1'>
                <Image src='/arrow.png' fill />
                </div>
            </div>
            
            <h2 className=' mt-20 font-bold text-[2.6rem]'>Overcome your biggest networking issues</h2>
            <p className=' w-[600px] text-center mt-4'>
                The ultimate email scraping solution! With its advanced technology,
                easily collect email addresses from various sources and reach out to
                potential customers or partners. Streamline your business processes 
                and boost your productivity.
            </p>
            </div>
        </div>        
    </>
    
)

export default Hero