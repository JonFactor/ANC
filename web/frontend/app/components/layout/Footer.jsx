import Link from 'next/link'
import React from 'react'


const Footer = () => {
  return (
    <div className=' w-full flex flex-col mt-12'>
        <div className=' w-screen bg-white h-[2px]' />
        <div className=' flex flex-row mt-4'>
            <div className=' flex flex-row'>
                <Link href='/' className=' font-semibold ml-8 text-2xl'>COSMOBOT</Link>
                <p className=' self-end text-xs ml-4'>What are you waiting for?</p>
            </div>
            <div className=' flex flex-row font-semibold self-end space-x-8 ml-[1300px]'>
                <Link href='/'>About</Link>
                <Link href='/'>Support</Link>
                <Link href='/'>Products</Link>
            </div>
        </div>
    </div>
  )
}

export default Footer