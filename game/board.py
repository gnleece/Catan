class Resources:
    Clay, Wood, Sheep, Wheat, Ore, Desert = range(6)
    Tiles = [ Clay, Clay, Clay,
              Wood, Wood, Wood, Wood,
              Sheep, Sheep, Sheep, Sheep,
              Wheat, Wheat, Wheat, Wheat,
              Ore, Ore, Ore,
              Desert
            ]
    Rolls = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    

class Hexagon():
    def __init__(self, id, vertices):
        self.id = id
        self.vertices = vertices # should be in clockwise order starting with upper left
        self.robber = False
        
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_tile(self, resource, tile_image, roll, roll_image=None):
        self.resource = resource
        self.tile_image = tile_image
        self.roll = roll
        self.roll_image = roll_image
    
    def draw(self, screen):
        screen.blit(self.tile_image,(self.x, self.y))
        if self.roll_image is not None:
            screen.blit(self.roll_image,(self.x+37, self.y+32))
        
    def draw_vertices(self, screen, img):
        screen.blit(img,(self.x+17, self.y-5))
        screen.blit(img,(self.x+75, self.y-5))
        screen.blit(img,(self.x+95, self.y+38))
        screen.blit(img,(self.x+75, self.y+83))
        screen.blit(img,(self.x+17, self.y+83))
        screen.blit(img,(self.x-5, self.y+38))
        
        
        
class Vertex():
    def __init__(self, id):
        self.id = id
        self.neighbours = set()
        self.x = None
        self.y = None

    def set_pos(self, x, y):
        self.x = x
        self.y = y
    
    def add_neighbour(self, neighbour_id):
        assert(len(self.neighbours) < 3)
        self.neighbours.add(neighbour_id)
        

    def draw_neighbourhood(self, screen, img1, img2, board):
        screen.blit(img1, (self.x, self.y))
        for neighbour in self.neighbours:
            screen.blit(img2, (board.vertices[neighbour].x, board.vertices[neighbour].y))
        
class Board:
    def __init__(self, size):
        self.init_vertices(size)
        self.init_hexagons(size)

    # standard Catan size is 3
    def init_vertices(self, size):
        ''' Calculates the neighbours of each vertex '''
        self.vertices = []
        cur_max = 6
        cur_min = 0
        vertices = {}
        back_edges = {}
        for x in range (1, size+1):
            y = (2*x - 1)*6
            
            if x < size:
                fwd_start = cur_max
                fwd_end = cur_max + (2*(x+1) -1)*6
                forwards = []
                cong = set(range(3, 2*x, 2))
                cong.add(0)
                for i in range(fwd_start, fwd_end):
                    remainder = i%(2*(x+1)-1)
                    if remainder in cong:
                        forwards.append(i)
            
            for n in range(cur_min, cur_max):
                vertex = Vertex(n)
                
                neighbour = ((n-cur_min) + 1)%y + cur_min
                vertex.add_neighbour(neighbour) 
                neighbour = ((n-cur_min) - 1)%y + cur_min
                vertex.add_neighbour(neighbour)
                
                if n in back_edges:
                    vertex.add_neighbour(back_edges[n])
                elif x < size:
                    neighbour = forwards[0]
                    if len(forwards) > 1:
                        forwards = forwards[1:]
                    vertex.add_neighbour(neighbour)
                    back_edges[neighbour] = n
                
                self.vertices.append(vertex)
                print str(n) + ": " + str(self.vertices[n].neighbours)
                
                
            cur_min = cur_max
            cur_max += (2*(x+1) -1)*6
            print ""

            
    def init_hexagons(self, size):
        self.hexagons = []
        
        self.hexagons.append(Hexagon(0, [27,28,8,7,25,26]))
        self.hexagons.append(Hexagon(1, [25,7,6,23,53,24]))
        self.hexagons.append(Hexagon(2, [53,23,22,50,51,52]))
        
        self.hexagons.append(Hexagon(3, [29,30,10,9,8,28]))
        self.hexagons.append(Hexagon(4, [8,9,1,0,6,7]))
        self.hexagons.append(Hexagon(5, [6,0,5,21,22,23]))
        self.hexagons.append(Hexagon(6, [22,21,20,48,49,50]))
        
        self.hexagons.append(Hexagon(7, [31,32,33,11,10,30]))
        self.hexagons.append(Hexagon(8, [10,11,12,2,1,9]))
        self.hexagons.append(Hexagon(9, [1,2,3,4,5,0]))
        self.hexagons.append(Hexagon(10, [5,4,18,19,20,21]))
        self.hexagons.append(Hexagon(11, [20,19,45,46,47,48]))
        
        self.hexagons.append(Hexagon(12, [33,34,35,13,12,11]))
        self.hexagons.append(Hexagon(13, [12,13,14,15,3,2]))
        self.hexagons.append(Hexagon(14, [3,15,16,17,18,4]))
        self.hexagons.append(Hexagon(15, [18,17,43,44,45,19]))
        
        self.hexagons.append(Hexagon(16, [35,36,37,38,14,13]))
        self.hexagons.append(Hexagon(17, [14,38,39,40,16,15]))
        self.hexagons.append(Hexagon(18, [16,40,41,42,43,17]))
        
    def finalize(self):     
        for hexagon in self.hexagons:
            self.vertices[hexagon.vertices[0]].set_pos(hexagon.x+17, hexagon.y-5)
            self.vertices[hexagon.vertices[1]].set_pos(hexagon.x+75, hexagon.y-5)
            self.vertices[hexagon.vertices[2]].set_pos(hexagon.x+95, hexagon.y+38)
            self.vertices[hexagon.vertices[3]].set_pos(hexagon.x+75, hexagon.y+83)
            self.vertices[hexagon.vertices[4]].set_pos(hexagon.x+17, hexagon.y+83)
            self.vertices[hexagon.vertices[5]].set_pos(hexagon.x-5, hexagon.y+38)
    
    def draw_vertices(self, screen, img):
        for vertex in self.vertices:
            screen.blit(img,(vertex.x, vertex.y))
        
                
                