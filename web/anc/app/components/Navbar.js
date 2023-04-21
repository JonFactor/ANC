'use client'
import Link from "next/link"

export default function Navbar() {

    return (
        <nav className=" space-x-6 ml-12">
            <Link href=" / " >Home</Link>
            <Link href=" / " >Login</Link>
            <Link href=" / " >Logout</Link>
            <Link href=" / " >LogUp</Link>
        </nav>
    )
}