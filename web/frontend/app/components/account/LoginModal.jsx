import Link from 'next/link'
import React from 'react'
import Image from 'next/image'

const LoginModal = () => {
  return (
    <div className=' w-[550px] h-[525px] bg-black bg-opacity-50 rounded-3xl'>
        <div className=' p-12 flex items-center justify-center flex-col '>
            <div className='items-center justify-center flex flex-col'>
                <h1 className=' text-3xl font-semibold mt-8'>Log In</h1>
                <h2 className=' text-lg mt-2 text-zinc-300'>Welcome back to Cosmobot</h2>
                <div className=' -mt-1 flex flex-row'>
                    <h3 className=' text-zinc-600 font-semibold '>Don't have an account? </h3>
                    <Link href="/" className=' text-purple-700 font-semibold ml-2 hover:underline'> Sign Up </Link>
                </div>
            </div>
            <div className=' flex flex-col'>
              <form action='post' className=' flex flex-col text-zinc-600 mt-6 '>
                <h3 className=' text-zinc-400 '> Log In with your email</h3>
                <input type="email" placeholder='name@example.com' className=' mt-1 bg-transparent border-[2px] border-zinc-600 w-80 px-2 py-1 pt-2 rounded-lg h-12'></input>
                <button type='submit' className=' text-white text-lg font-semibold bg-[#5A42D4] h-12 rounded-lg mt-2'>Continue</button>
              </form>
              <div className=' flex flex-row text-zinc-400 justify-items-center items-center space-x-2'>
                <div className=' w-36 h-[1px] bg-zinc-500 ' />
                <h4 className=' text-zinc-500'>Or</h4>
                <div className=' w-36 h-[1px] bg-zinc-500 ' />
              </div>
              <div className=' bg-black opacity-100'>
                <button className=' flex flex-row items-center justify-center border-2 border-zinc-600 py-2 rounded-lg w-full'>
                  <div className=' relative w-8 aspect-square'>
                    <Image fill src='/goal.png'></Image>
                  </div>
                  <p>Log In with Google</p>
                </button>                              
              </div>
            </div>

        </div>
    </div>
  )
}

export default LoginModal