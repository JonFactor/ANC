import React from 'react'
import Link from 'next/link'


const Quickstart = () => {



  return (
        <div id='section-2' className=' flex flex-row relative '>
            <div className=' flex flex-col items-center w-screen'>
                <div className=' mt-12 flex flex-row'>
                    <Link href='/' className=' text-lg text-[#5A42D4] hover:underline font-semilight' >View our quick start guide &#8594;</Link>
                </div>   
                <h2 className=' mt-20 font-bold text-[2.6rem]'>Overcome your biggest networking issues</h2>
                <div className=' w-[700px] text-center mt-4 space-y-2 font-light text-lg'>
                    <p>
                        The ultimate email scraping solution! With its advanced technology,
                        easily collect 
                    </p>
                    <p> 
                        email addresses from various sources and reach out to
                        potential customers or
                    </p>
                    <p> 
                        partners. Streamline your business processes 
                        and boost your productivity.
                    </p>                
                </div>
                <div className=' mt-12 flex flex-row space-x-8'>
                    <button className=' rounded-3xl bg-purple-700 w-44 h-12'> How it all works</button>
                    <button className=' rounded-3xl border-[#5A42D4] border-2 w-44 h-12'> Ease of use</button>
                    <button className=' rounded-3xl border-[#5A42D4] border-2 w-44 h-12'> Create links</button>
                </div>
                <div className=' flex flex-row space-x-24 mt-24'>
                    <div className=' flex flex-col space-y-12'>
                        <div>
                            <h2 className=' text-2xl font-semibold'> How it Works </h2>
                            <p className=' w-[500px] font-light mt-2'>
                            Introducing Cosmobot - your ultimate email discovery 
                            tool! With just a simple search term of your choice, 
                            our advanced technology scours the web to retrieve 
                            the most relevant and valuable email addresses related to your request.
                            </p>
                        </div>
                        <div className=' rounded-lg bg-black bg-opacity-30 w-[500px] h-36 border-2 border-white border-opacity-10 '>
                            <div className=' p-4 opacity-100 text-white flex flex-row'>
                                <div className=' flex flex-col'>
                                    <h3 className=' font-semibold' >Selenium Automation</h3>
                                    <p className=' font-light mt-2 w-[400px] text-sm'>
                                        Selenium is an open source project for a 
                                        range of tools and libraries aimed at supporting 
                                        browser automation.
                                    </p>                                    
                                </div>
                                <Link href="/" className=' text-3xl text-purple-700 mt-8 ml-8' >&#8594;</Link>
                            </div>
                        </div>
                    </div>
                    <div className=' bg-black w-[550px] h-[550px] 
                    rounded-tl-[150px] rounded-br-[150px] rounded-tr-3xl rounded-bl-3xl
                    opacity-25 border-2 border-white border-opacity-30'>
                    </div>
                </div>
            </div>
        </div>        
  )
}

export default Quickstart