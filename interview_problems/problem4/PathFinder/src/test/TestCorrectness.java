package test;
import org.junit.*;
import java.util.*;

public class TestCorrectness extends AbstractTest
{
	@Test
	public void example1()
	{
		List<Integer> list = Arrays.asList(1, 2, 0);
		int pos = 0;
		test(list, pos);
	}

	@Test
	public void example2()
	{
		List<Integer> list = Arrays.asList(2, 3, 0, 2, 2);
		int pos = 0;
		test(list, pos);
	}

	@Test
	public void example3()
	{
		List<Integer> list = Arrays.asList(2, 1, 0);
		int pos = 0;
		test(list, pos, -1);
	}
}
