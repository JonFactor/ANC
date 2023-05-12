import Footer from './components/layout/Footer'
import Navbar from './components/layout/Navbar'
import './globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body className=' bg-[#0D0618] text-white overflow-x-hidden  '>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  )
}
