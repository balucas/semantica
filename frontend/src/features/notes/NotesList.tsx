import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useQuery } from '@tanstack/react-query'
import { Card, CardContent, Typography, Grid } from '@mui/material'
import { notesApi } from '@/api/notes'
import { RootState } from '@/store'
import { setLoading, setError } from './notesSlice'

export const NotesList = () => {
  const dispatch = useDispatch()
  const notes = useSelector((state: RootState) => state.notes.items)

  const { data, isLoading, error } = useQuery({
    queryKey: ['notes'],
    queryFn: () => notesApi.searchNotes(''),
  })

  useEffect(() => {
    dispatch(setLoading(isLoading))
    if (error) {
      dispatch(setError(error instanceof Error ? error.message : 'An error occurred'))
    }
  }, [dispatch, isLoading, error])

  if (isLoading) {
    return <Typography>Loading notes...</Typography>
  }

  if (error) {
    return <Typography color="error">Error loading notes</Typography>
  }

  return (
    <Grid container spacing={2}>
      {notes.map((note) => (
        <Grid item xs={12} key={note.id}>
          <Card>
            <CardContent>
              <Typography variant="h6">{note.content}</Typography>
              <Typography variant="caption" color="text.secondary">
                {new Date(note.createdAt).toLocaleDateString()}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  )
} 