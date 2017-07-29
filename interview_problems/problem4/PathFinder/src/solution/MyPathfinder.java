package solution;
import java.util.List;
import java.util.ArrayList;

import problem.Pathfinder;

public class MyPathfinder extends Pathfinder
{
	public void SolutionPathFinder(List<Integer> inpList, List<Integer> outList, 
			List<List<Integer>> pathList, int pos, List<Integer> visitedList) {
		
		if(pos == inpList.size()) {
	       List<Integer> newList = new ArrayList<Integer>();
	       newList.addAll(outList);
	       pathList.add(newList);
	       return;
	   } else if (pos > inpList.size() || pos < 0) {
    	   return;
	   } else if ((inpList.get(pos) == null) || (inpList.get(pos) == 0)) {
	       return;
	   } else if (visitedList.contains(pos)) {
	      return;
	   } else {
		   visitedList.add(pos);
		   if(inpList.get(pos) >= 0){
			   for(int i = 1; i<=inpList.get(pos); i++)
		       {
		           outList.add(i);
		           SolutionPathFinder(inpList, outList, pathList, pos + i, visitedList);
		           outList.remove(outList.size() - 1);
		       }      
		   } else {
			   for(int i = inpList.get(pos); i < 0; i++)
		       {
				   outList.add(i);
		           SolutionPathFinder(inpList, outList, pathList, pos + i, visitedList);
		           outList.remove(outList.size() - 1);
		       }
		   }
           visitedList.remove(visitedList.size() - 1);
	   }	   
	}
	
	@Override
	public List<Integer> findPath(List<Integer> inList, int pos)
	{
		// TODO Auto-generated method stub
		if(inList == null)
			return null;
		else if(inList.size() == 0)
			return inList;
		
		if(pos < 0) {
			return null;
		}
		
		List<Integer> outList = new ArrayList<Integer>();
		List<Integer> visitedList = new ArrayList<Integer>();
		List<List<Integer>> pathList = new ArrayList<List<Integer>>();
		SolutionPathFinder(inList, outList, pathList, pos, visitedList);
		
		if(pathList.size() == 0)
			return null;
		int minLen = Integer.MAX_VALUE;
		List<Integer> finalList = new ArrayList<Integer>();
		for(int i=0; i< pathList.size(); i++)
		{
		    if (pathList.get(i).size() < minLen)
		    {
		       minLen = pathList.get(i).size();
		       finalList = pathList.get(i);
		    }  
		}
		
		return finalList;
	}
}
