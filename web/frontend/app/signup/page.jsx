import React from 'react'
import BackroundAbsolutesAccounts from '../components/account/BackroundAbsolutesAccounts'
import SignupModal from '../components/account/SignupModal'

const page = () => {
  return (
    <>
    <div className=' absolute'>
        <BackroundAbsolutesAccounts />
    </div>
    <div className=' px-64 py-36 flex flex-row space-x-36'>
        <div className=' flex flex-col'>
            <h1 className=' text-3xl font-light'>Sign Up</h1>
            <h2 className=' font-semibold text-5xl w-[600px]'>We see the future of communication and connections</h2>
            <div className=' flex flex-row mt-4 space-x-4'>
                <div className=' aspect-square w-2 rounded-full bg-zinc-600' />
                <div className=' aspect-square w-2 rounded-full bg-zinc-500' />
                <div className=' aspect-square w-2 rounded-full bg-zinc-200' />
            </div>
        </div>
        <SignupModal />
    </div>
    </>
  )
}

export default page