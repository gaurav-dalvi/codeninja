import json
import sys

SUCCESS_RESPONSE = json.dumps({"ok": True})
FAILURE_RESPONSE = json.dumps({"ok": False})

class Node:

    def __init__(self, id, name, parentID):
        self.id = id
        self.name = name
        self.parentID = parentID
        self.children = None

    def getID(self):
        return self.id

    def getParentID(self):
        return self.parentID

    def getName(self):
        return self.name

    def getChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = children

class Hierarchy:

    def __init__(self):
        self.head = None
        self.hashMap = {}

    def PrintTree(self, head, nodeList):
        temp = head
        if temp is not None:
            #print temp.getID(), temp.getName(), temp.getParentID()
            nodeList.append(temp)
            sib = temp.getChildren()
            if sib is not None:
                for i in xrange(len(sib)):
                    self.PrintTree(sib[i], nodeList)

    # Searching in tree by id of Node
    def SearchbyID(self, node, id):

        if node is None:
            return None
        elif node.getID() == id:
            return node
        else:
            sib = node.getChildren()
            if sib is not None:
                for i in xrange(len(sib)):
                    temp = self.SearchbyID(sib[i], id)
                    if temp is not None:
                        return temp


    # Searching in tree by name of the Node
    def SearchbyName(self, node, name):

        if node is None:
            return None
        elif node.getName() == name:
            return node
        else:
            sib = node.getChildren()
            if sib is not None:
                for i in xrange(len(sib)):
                    temp = self.SearchbyName(sib[i], name)
                    if temp is not None:
                        return temp

    def Add_Node(self, node):

        if self.head is None:
            if node.getParentID() != "":
                print >> sys.stderr, 'Adding node nonexistent parent'
                return FAILURE_RESPONSE
            else:
                self.head = node
                self.hashMap[node.getID()] = True
                return SUCCESS_RESPONSE
        elif node.getID() in self.hashMap.keys():
            print >> sys.stderr, 'ID must be unique in the entire Tree'
            return FAILURE_RESPONSE
        else:
            parentID = node.getParentID()
            temp = self.SearchbyID(self.head, parentID)
            if temp is None:
                print >> sys.stderr, 'the parentID specified does not exist in tree'
                return FAILURE_RESPONSE
            else:
                sib = temp.getChildren()
                if sib is None:
                    sib = []
                for i in xrange(len(sib)):
                    if sib[i].getName() == node.getName():
                        print >> sys.stderr, 'Siblings can not have same name'
                        return FAILURE_RESPONSE
                sib.append(node)
                # # sort siblings lists by names
                # sib = sorted(sib, key = lambda node: node.getName())

                temp.setChildren(sib)
                self.hashMap[node.getID()] = True
                print >> sys.stderr, 'Successfully added node'
                return SUCCESS_RESPONSE


    def Delete_Node(self, nodeID):

        if nodeID == '':
            print >> sys.stderr, 'ID must be specified and not an empty string.'
            return FAILURE_RESPONSE
        elif nodeID not in self.hashMap.keys():
            print >> sys.stderr, 'nodeID is not in tree. It must exists'
            return FAILURE_RESPONSE

        temp = self.SearchbyID(self.head, nodeID)
        if temp is None:
            print >> sys.stderr, 'Node must exist'
            return FAILURE_RESPONSE
        elif temp.getChildren() is not None:
            print >> sys.stderr, 'Node must not have children'
            return FAILURE_RESPONSE
        else:
            parentID = temp.getParentID()
            parent = self.SearchbyID(self.head, parentID)
            sib = parent.getChildren()
            for i in xrange(len(sib)):
                if sib[i].getID() == nodeID:
                    sib.remove(sib[i])
                    self.hashMap.pop(nodeID)
                    # # sort siblings lists by names
                    # sib = sorted(sib, key=lambda node: node.getName())
                    return SUCCESS_RESPONSE
            print >> sys.stderr, 'node is not preset in siblings'
            return FAILURE_RESPONSE

    def StorePathFromRoot(self, root, nodeID, pathList, index):
        if root == None:
            return (None, 0)
        pathList[index] = root.getID()
        index += 1

        if root.getID() == nodeID:
            return (root, index)
        else:

            sib = root.getChildren()
            if sib is not None:
                for i in xrange(len(sib)):
                    (node, index1) = self.StorePathFromRoot(sib[i], nodeID, pathList, index)
                    if node is not None:
                        return (node, index1)

        return (None, 0)


    def Move_Node(self, nodeID, newParentID):

        if nodeID is None or newParentID == None or nodeID == '' or newParentID == '':
            print >> sys.stderr, 'nodeID or newParentID can not empty string'
            return FAILURE_RESPONSE

        newParentNode = self.SearchbyID(self.head, newParentID)
        node = self.SearchbyID(self.head, nodeID)
        curr_parentID = node.getParentID()
        curr_parentNode = self.SearchbyID(self.head, curr_parentID)

        if newParentNode is None or node is None:
            print >> sys.stderr, 'nodeID or newParentID must be present in the tree'
            return FAILURE_RESPONSE

        # Detecting Cycle
        myList = [0] * 1000
        # get Path of newParentID from head node.
        (temp, index) = self.StorePathFromRoot(self.head, newParentID, myList, 0)
        for i in xrange(index):
            if myList[i] == nodeID:
                print >> sys.stderr, 'Cycle detected in the tree. Can not move the node'
                return FAILURE_RESPONSE

        sib = newParentNode.getChildren()

        if sib is not None:
            for i in sib:
                if i.getID() == nodeID:
                    print >> sys.stderr, 'Siblings can not have same names'
                    return FAILURE_RESPONSE

        # remove Node
        self.Delete_Node(nodeID)
        # add node in the tree
        newNode = Node(nodeID, node.getName(), newParentID)
        self.Add_Node(newNode)

        return SUCCESS_RESPONSE

    def minDepth(self, min_depth, opList, node, curr_depth):

        if node is None:
            return
        if curr_depth >= min_depth:
            opList.append(node)

        sib = node.getChildren()
        if sib is not None:
            for i in sib:
                self.minDepth(min_depth, opList, i, curr_depth + 1)

    def maxDepth(self, max_depth, opList, node, curr_depth):

        if node is None:
            return
        if curr_depth <= max_depth:
            opList.append(node)

        sib = node.getChildren()
        if sib is not None:
            for i in sib:
                self.maxDepth(max_depth, opList, i, curr_depth + 1)

    def minDepthQuery(self, rootIdsList, minDepthVal, nodeList):

        # Evaluate minDepth
        if rootIdsList is not None:
            for i in rootIdsList:
                temp = tree.SearchbyID(tree.head, i)
                if temp is not None:
                    myList = []
                    tree.minDepth(minDepthVal, myList, temp, 0)
                    for i in myList:
                        nodeList.append(i)
        else:
            temp = tree.head
            if temp is not None:
                myList = []
                tree.minDepth(minDepthVal, myList, temp, 0)
                for i in myList:
                    nodeList.append(i)

    def maxDepthQuery(self, rootIdsList, maxDepthVal, nodeList):

        # Evaluate minDepth
        if rootIdsList is not None:
            for i in rootIdsList:
                temp = tree.SearchbyID(tree.head, i)
                if temp is not None:
                    myList = []
                    tree.maxDepth(maxDepthVal, myList, temp, 0)
                    for i in myList:
                        nodeList.append(i)
        else:
            temp = tree.head
            if temp is not None:
                myList = []
                tree.maxDepth(maxDepthVal, myList, temp, 0)
                for i in myList:
                    nodeList.append(i)

    def EvaluateQuery(self, namesList, idsList, rootIdsList, minDepthVal, maxDepthVal):

        resultDict = {"nodes": []}
        nodeList = []

        if namesList is None and idsList is None and rootIdsList is None and minDepthVal is None and maxDepthVal is None:
            # print full tree
            tree.PrintTree(tree.head, nodeList)
            if nodeList is None:
                print json.loads(resultDict)
            else:
                for node in nodeList:
                    temp = {"id": str(node.getID()), "name": str(node.getName()), "parent_id": str(node.getParentID())}
                    resultDict['nodes'].append(temp)
                print str(resultDict)
                return
        else:

            if minDepthVal is not None:
                tree.minDepthQuery(rootIdsList, minDepthVal, nodeList)

            if maxDepthVal is not None:
                tree.maxDepthQuery(rootIdsList, maxDepthVal, nodeList)

            # handling for namesList
            tempList = []
            if namesList is not None:
                for name in namesList:
                    for obj in nodeList:
                        if name == obj.getName():
                            tempList.append(obj)

                nodeList = tempList

            # handling for idsList:
            tempList = []
            if idsList is not None:
                for id in idsList:
                    for obj in nodeList:
                        if id == obj.getID():
                            tempList.append(obj)

                nodeList = tempList

            for node in nodeList:
                temp = {}
                temp['id'] = node.getID()
                temp['name'] = node.getName()
                temp['parent_id'] = node.getParentID()
                resultDict['nodes'].append(temp)
            print str(resultDict)
            return


if __name__ == '__main__':

    tree = Hierarchy()
    namesList = None
    idsList = None
    rootIdsList = None
    minDepth = None
    maxDepth = None

    while True:
        input_str = raw_input()

        if input_str is None or input_str == '':
            break

        #Convert Input json string to dictionary
        json_dict = json.loads(input_str)

        if 'add_node' in json_dict.keys():
            id = json_dict['add_node']['id']
            name = json_dict['add_node']['name']
            if 'parent_id' not in json_dict['add_node'].keys():
                node = Node(id, name, "")
                print tree.Add_Node(node)
            else:
                node = Node(id, name, json_dict['add_node']['parent_id'])
                print tree.Add_Node(node)

        elif 'delete_node' in json_dict.keys():
            id = json_dict['delete_node']['id']
            print tree.Delete_Node(id)

        elif 'move_node' in json_dict.keys():
            id = json_dict['move_node']['id']
            new_parent_id = json_dict['move_node']['new_parent_id']
            print tree.Move_Node(id, new_parent_id)

        elif 'query' in json_dict.keys():
            if 'names' in json_dict['query'].keys():
                namesList = json_dict['query']['names']

            if 'ids' in json_dict['query'].keys():
                idsList = json_dict['query']['ids']

            if 'root_ids' in json_dict['query'].keys():
                rootIdsList = json_dict['query']['root_ids']

            if 'min_depth' in json_dict['query'].keys():
                minDepth = json_dict['query']['min_depth']

            if 'max_depth' in json_dict['query'].keys():
                maxDepth = json_dict['query']['max_depth']

            tree.EvaluateQuery(namesList, idsList, rootIdsList, minDepth, maxDepth)

        else:
            print >> sys.stderr, 'Operation not supported'

    print >> sys.stderr, 'Exiting the program'



