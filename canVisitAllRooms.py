class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms ==[]:
            return True
        vistedRoom = [0]
        currentRoom = 0
        roomsNum = len(rooms)

        def dps(currentroom,vistedRoom,rooms):
            if rooms[0] ==[]:
                if len(vistedRoom) == roomsNum:
                    return True
                else:
                    return False
                
            if rooms[currentroom] == []:
                return
            for nextRoom in rooms[currentroom]:
                if nextRoom not in vistedRoom:
                    currentroom = nextRoom
                    vistedRoom.append(nextRoom)
                    dps(currentroom,vistedRoom,rooms)
                else:
                    continue
            if len(vistedRoom) == roomsNum:
                return True
            else:
                return False
        return dps(currentRoom,vistedRoom,rooms)