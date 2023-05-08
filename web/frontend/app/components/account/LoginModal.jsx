import Link from 'next/link'
import React from 'react'

const LoginModal = () => {
  return (
    <div className=' w-[550px] h-[525px] bg-black bg-opacity-50 rounded-3xl border-2 border-white border-opacity-5'>
        <div className=' p-12 flex items-center justify-center flex-col '>
            <div className='items-center justify-center flex flex-col'>
                <h1 className=' text-2xl font-semibold mt-8'>Log In</h1>
                <h2 className=' text-lg mt-2 text-zinc-300'>Welcome back to Cosmobot</h2>
                <div className=' flex flex-row'>
                    <h3 className=' text-zinc-600 font-semibold '>Don't have an account? </h3>
                    <Link href="/" className=' text-purple-700 font-semibold ml-2 hover:underline'> Sign Up </Link>
                </div>
            </div>
            <div>

            </div>
        </div>
    </div>
  )
}

export default LoginModal