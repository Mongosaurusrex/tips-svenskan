import React, { useState, useEffect } from "react";

import { DragDropContext, Draggable, Droppable } from "react-beautiful-dnd";
import { getThisSeasonsTeams } from "../api/teams";

function DragAndDropTable() {
  const [teams, setTeams] = useState([]);
  useEffect(() => {
    async function fetchTeams() {
      let thisSeasonsTeams = await getThisSeasonsTeams();
      setTeams(thisSeasonsTeams);
    }

    fetchTeams();
  }, []);
  function handleOnDragEnd(result) {
    if (!result.destination) return;
    const items = Array.from(teams);
    const [reorderedItem] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, reorderedItem);

    setTeams(items);
  }

  const StrictModeDroppable = ({ children, ...props }) => {
    const [enabled, setEnabled] = useState(false);

    useEffect(() => {
      const animation = requestAnimationFrame(() => setEnabled(true));

      return () => {
        cancelAnimationFrame(animation);
        setEnabled(false);
      };
    }, []);

    if (!enabled) {
      return null;
    }

    return <Droppable {...props}>{children}</Droppable>;
  };

  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="min-w-screen p-5 rounded shadow-md w-2/3">
        <h2 className="text-2xl font-bold text-white mb-4 text-center">
          Din tabell
        </h2>
        <table className="table-auto w-full">
          {!!teams && (
            <DragDropContext onDragEnd={handleOnDragEnd}>
              <StrictModeDroppable droppableId="teams">
                {(provided) => (
                  <tbody {...provided.droppableProps} ref={provided.innerRef}>
                    {teams.map(({ id, logo, name }, index) => (
                      <Draggable
                        key={id}
                        draggableId={index.toString()}
                        index={index}
                      >
                        {(provided) => (
                          <tr
                            className={`bg-${
                              index % 2 === 0 ? "[#12326e]" : "[#ffffff]"
                            } text-white ${
                              index === 2 && "border-b-2 border-[#fcb900]"
                            } ${
                              index === 13 &&
                              "border-b-2 border-t-2 border-[#fcb900]"
                            }`}
                            ref={provided.innerRef}
                            {...provided.draggableProps}
                            {...provided.dragHandleProps}
                          >
                            <td className="px-4 py-2 flex items-center">
                              <img src={logo} alt={name} className="h-6 mr-2" />
                              {name}
                            </td>
                          </tr>
                        )}
                      </Draggable>
                    ))}
                  </tbody>
                )}
              </StrictModeDroppable>
            </DragDropContext>
          )}
        </table>
      </div>
    </div>
  );
}

export default DragAndDropTable;
