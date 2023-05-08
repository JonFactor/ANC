import React from 'react'
import LoginModal from '../components/account/LoginModal'

const page = () => {
  return (
    <>
      <div className=' absolute'> 
        <div id='blue-blur' className='absolute  bg-blue-400 blur-[250px] opacity-25 w-[806px] h-[650px] ml-[1300px] -mt-[337px]' />
        <div id='purp-blur' className='absolute  bg-[#BA21AB] blur-[200px] opacity-25 w-[706px] h-[600px] -ml-[150px] mt-[137px]' />
        <div id='purp-blur' className='absolute  bg-green-500 blur-[200px] opacity-30 w-[906px] h-[700px] ml-[250px] mt-[437px]' />
        <div id='purp-blur' className='absolute  bg-purple-500 blur-[200px] opacity-25 w-[706px] h-[600px] ml-[1250px] mt-[637px]' />
      </div>
      <div className=' px-64 py-36 flex flex-row space-x-36'>
        <div className=' flex flex-col'>
          <h1 className=' text-3xl font-light'>Log In</h1>
          <h2 className=' font-semibold text-5xl w-[600px]'>We see the future of communication and connections</h2>
          <div className=' flex flex-row mt-4 space-x-4'>
            <div className=' aspect-square w-2 rounded-full bg-zinc-600' />
            <div className=' aspect-square w-2 rounded-full bg-zinc-500' />
            <div className=' aspect-square w-2 rounded-full bg-zinc-200' />
          </div>
        </div>
        <LoginModal />
      </div>
    </>
  )
}

export default page