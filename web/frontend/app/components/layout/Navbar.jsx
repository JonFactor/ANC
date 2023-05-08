import Link from 'next/link'
import React from 'react'

const Navbar = () => {
  return (
    <div className=' flex flex-row p-4'>
        <Link href='/' className=' ml-12 font-bold text-2xl ' >COSMOBOT</Link>
        <div className=' flex flex-row text-lg  font-semibold space-x-12 self-end ml-[1250px] z-50'>
            <Link href='/'>about</Link>
            <Link href='/pricing'>pricing</Link>
            <Link href='/'>contact</Link>
            <Link href='/login'>Log In</Link>
        </div>
    </div>
  )
}

export default Navbar