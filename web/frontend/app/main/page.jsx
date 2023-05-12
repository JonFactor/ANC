'use client'
import React, { useEffect, useState } from 'react'
import useAxios from '../utils/useAxios'

const page = () => {
  const [res, setRes] = useState("")
  const api = useAxios()
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get("/test/")
        setRes(response.data.response)
      } catch {
        setRes("ERROR IN FETCHDATA")
      }
    }
  }, [])
  return (
    <div>

    </div>
  )
}

export default page