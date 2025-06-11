import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useQuery } from '@tanstack/react-query'
import { Card, CardContent, Typography, List, ListItem, ListItemText, Divider } from '@mui/material'
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
    <List>
      {notes.map((note, index) => (
        <div key={note.id}>
          <ListItem>
            <ListItemText
              primary={note.content}
              secondary={new Date(note.createdAt).toLocaleDateString()}
              primaryTypographyProps={{
                sx: { 
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  display: '-webkit-box',
                  WebkitLineClamp: 2,
                  WebkitBoxOrient: 'vertical',
                }
              }}
            />
          </ListItem>
          {index < notes.length - 1 && <Divider />}
        </div>
      ))}
    </List>
  )
} 