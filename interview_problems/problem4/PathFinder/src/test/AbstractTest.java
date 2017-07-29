package test;
import static org.junit.Assert.fail;

import java.util.List;

import problem.Pathfinder;
import solution.MyPathfinder;

abstract class AbstractTest
{
	public void test(List<Integer> list, int pos)
	{
		test(list, pos, list != null ? list.size() : -1);
	}

	public void test(List<Integer> list, int pos, int threshold)
	{
		Pathfinder pathfinder = new MyPathfinder();
		List<Integer> path = pathfinder.findPath(list, pos);
		String validation = validateResult(list, pos, path, threshold);

		if (validation != null)
		{
			StringBuffer error = new StringBuffer("\n");
			error.append("list: ").append(list).append("\n");
			error.append("pos: ").append(pos).append("\n");
			error.append("findPath returned: ").append(path).append("\n");
			error.append("ERROR: ").append(validation);
			fail(error.toString());
		}
	}
	
	private static String validateResult(List<Integer> list, int pos, List<Integer> path, int threshold)
	{
		String validation = null;
		if (path == null)
		{
			if (threshold >= 0)
			{
				validation = "null value returned when valid path exists";
			}
		}
		else if (threshold < 0)
		{
			validation = "non-null value returned when no valid path exists";
		}
		else
		{
			validation = validatePath(list, pos, path);
			
			if (validation == null && path.size() > threshold)
			{
				validation = "path of length " + path.size() + " provided, but shorter path of length " + threshold + " exists";
			}
		}

		return validation;
	}

	private static String validatePath(List<Integer> list, int pos, List<Integer> path)
	{
		// check inputs
		if (list == null || path == null || pos < 0 || pos > list.size())
		{
			throw new IllegalArgumentException("unexpected input: " + pos + " " + list + " " + path);
		}

		String invalid = "invalid jump at position " + pos + ": ";

		if (pos == list.size() && path.isEmpty())
		{
			// success!
			return null;
		}
		else if (pos == list.size() && !path.isEmpty())
		{
			// jump when at end of list
			return invalid + path.get(0);
		}
		else if (path.isEmpty())
		{
			// no jump when not at end of list
			return "path ends at position " + pos;
		}
		else
		{
			Integer jump = path.get(0);
			Integer value = list.get(pos);

			if (jump == null)
			{
				// null value in path
				return invalid + "null";
			}
			else if (value == null)
			{
				// jump when value is null
				return invalid + "value is null";
			}
			else if (jump == 0)
			{
				// jump of 0
				return invalid + "0";
			}
			else if (value > 0 && jump > value)
			{
				// jump greater than positive value
				return invalid + jump + " > " + value;
			}
			else if (value >= 0 && jump < 0)
			{
				// jump less than zero for positive value
				return invalid + jump + " < 0";
			}
			else if (value < 0 && jump < value)
			{
				// jump less than negative value
				return invalid + jump + " < " + value;
			}
			else if (value <= 0 && jump > 0)
			{
				// jump greater than zero for negative value
				return invalid + jump + " > 0";
			}
			else if (pos + jump > list.size() || pos + jump < 0)
			{
				// jump to invalid position
				return invalid + "jump of " + jump + " leads to invalid position " + (pos + jump);
			}
			else
			{
				// valid jump, continue
				return validatePath(list, pos + jump, path.subList(1, path.size()));
			}
		}
	}
}
